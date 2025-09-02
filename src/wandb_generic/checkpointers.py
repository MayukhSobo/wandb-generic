import wandb
import yaml
import functools
import torch

class WandbGenericCheckpoint:
    def __init__(self, config_path):
        self.config_path = config_path

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            model = func(*args, **kwargs)

            with open(self.config_path, 'r') as f:
                config = yaml.safe_load(f)

            if 'checkpoint' in config and wandb.run is not None:
                checkpoint_config = config['checkpoint']
                artifact = wandb.Artifact(checkpoint_config['name'], type=checkpoint_config['type'])
                torch.save(model.state_dict(), "model.pth")
                artifact.add_file("model.pth")
                wandb.log_artifact(artifact)

            return model

        return wrapper
