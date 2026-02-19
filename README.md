### DeepSeek-OCR examples

Example application of running deepseek-ocr model

Original repo:
https://github.com/deepseek-ai/DeepSeek-OCR/tree/main


### On installing and running with vLLM

Deepseek-OCR support only added to vLLM version 0.11.0 which has a breaking change as it requires pytorch 2.9.0 which depends on CUDA > 12.2, which is the current laptop version...

The example meant to install 0.8.5 whl of vLLM and running the provided scripts instead... so will try that option until CUDA is updated...

https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-OCR.html#offline-ocr-tasks


### Running inside docker container

```
docker pull nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04

docker run -it --name devtest -v "$(pwd)"/examples:/examples --rm --gpus all nvidia/cuda:12.6.3-cudnn-devel-ubuntu22.04  /bin/bash
```

Error running inside docker container from torch:
```
RuntimeError: Unexpected error from cudaGetDeviceCount(). Did you run some cuda functions before calling NumCudaDevices() that might have already set an error? Error 804: forward compatibility was attempted on non supported HW
```

```
When the host outside the docker is running a driver that doesn't support the cuda version inside the container
```

Fixes for above ^:
* Updated host nvidia driver to at least 580
* Need to use pytorch version with cuda 12.6 for geforce gtx 1060 as it only has compute capability of 6.1?
  ```
  https://discuss.pytorch.org/t/what-version-of-pytorch-is-compatible-with-nvidia-geforce-gtx-1080/222056/5

  ```

Tried to run locally on GEFORCE GTX 1060 6GB model but still hit gpu memory constraint... need to try docker approach on VMs with more memory...


#### Running on Lambda labs

* Provision at least A10 GPU instance with Lambda Stack
* Add the ssh keys to your local ssh-agent
  ```
  ssh-add <path to private key path>
  ssh-add -L

  ssh ubuntu@<ip>
  ```
* Copy local files to remote instance:
  ```
  rsync -av --info=progress2 <FILES> <USERNAME>@<SERVER-IP>:<REMOTE-PATH>
  ```