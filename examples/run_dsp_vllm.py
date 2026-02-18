import argparse
from vllm import LLM, SamplingParams
from vllm.model_executor.models.deepseek_ocr import NGramPerReqLogitsProcessor
from PIL import Image


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", help="Path to image for inference")
    args = ap.parse_args()

    # Create model instance
    llm = LLM(
        model="deepseek-ai/DeepSeek-OCR",
        enable_prefix_caching=False,
        mm_processor_cache_gb=0,
        logits_processors=[NGramPerReqLogitsProcessor]
    )

    # Prepare batched input with your image file
    image_1 = Image.open(args.image).convert("RGB")
    prompt = "<image>\n<|grounding|>OCR this image."

    model_input = [
        {
            "prompt": prompt,
            "multi_modal_data": {"image": image_1}
        },
    ]

    sampling_param = SamplingParams(
                temperature=0.0,
                max_tokens=8192,
                # ngram logit processor args
                extra_args=dict(
                    ngram_size=30,
                    window_size=90,
                    whitelist_token_ids={128821, 128822},  # whitelist: <td>, </td>
                ),
                skip_special_tokens=False,
            )
    # Generate output
    model_outputs = llm.generate(model_input, sampling_param)

    # Print output
    for output in model_outputs:
        print(output.outputs[0].text)