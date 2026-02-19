#!/usr/bin/env bash

set -e

echo "Installing uv..."

apt update -y && apt install -y curl

curl -LsSf https://astral.sh/uv/install.sh | sh

source $HOME/.local/bin/env

uv python install cpython-3.12.12-linux-x86_64-gnu

# uv venv && source .venv/bin/activate

# uv pip install vllm --torch-backend=cu126