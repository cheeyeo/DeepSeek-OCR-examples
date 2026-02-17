import os
import argparse
from transformers import AutoModel, AutoTokenizer
import torch


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", help="Input image to OCR")
    args = ap.parse_args()

    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    model_name = 'deepseek-ai/DeepSeek-OCR'

    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    model = AutoModel.from_pretrained(model_name, _attn_implementation='flash_attention_2', trust_remote_code=True, use_safetensors=True)

    model = model.eval().cuda().to(torch.bfloat16)
    print(model)

    prompt = "<image>\n<|grounding|>OCR this image."
    image_file = args.image
    output_path = "processed"

    res = model.infer(tokenizer, prompt=prompt, image_file=image_file, output_path=output_path, base_size=1024, image_size=640, crop_mode=True, save_results=True, test_compress=True)

    print(res)