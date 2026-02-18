### DeepSeek-OCR examples

Example application of running deepseek-ocr model

Original repo:
https://github.com/deepseek-ai/DeepSeek-OCR/tree/main


### On installing and running with vLLM

Deepseek-OCR support only added to vLLM version 0.11.0 which has a breaking change as it requires pytorch 2.9.0 which deoends on CUDA > 12.2, which is the current laptop version...

The example meant to install 0.8.5 whl of vLLM and running the provided scripts instead... so will try that option until CUDA is updated...

https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-OCR.html#offline-ocr-tasks