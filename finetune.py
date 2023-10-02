import replicate

training = replicate.trainings.create(
    version="meta/llama-2-7b-chat:8e6975e5ed6174911a6ff3d60540dfd4844201974602551e10e9e87ab143d81e",
    input={
        "train_data": "https://gist.githubusercontent.com/nateraw/055c55b000e4c37d43ce8eb142ccc0a2/raw/d13853512fc83e8c656a3e8b6e1270dd3c398e77/samsum.jsonl",
        "num_train_epochs": 1
    },
    destination="juanjaragavi/abby-llama-2-7b-chat"
)

print(training)