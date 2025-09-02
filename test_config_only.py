"""
Test FIXED version - should only log metrics from config file!
"""

import random
import time
from wandb_generic import WandbGenericLogger

# YOUR EXACT CODE - Should only log: epoch, loss, accuracy (NO step!)
@WandbGenericLogger(config_path="examples/sample.config.yaml")
def train_model(wandb_run=None):
    """Should only log metrics from config: epoch, loss, accuracy."""
    print("🎯 Testing CONFIG-ONLY logging...")
    
    for i in range(6):
        epoch = i + 1
        loss = random.random()
        accuracy = random.random()
        print(f"Epoch {epoch}: loss={loss:.3f}, accuracy={accuracy:.3f}")
        time.sleep(0.2)
    
    return "Config-only test completed!"

if __name__ == "__main__":
    print("🔍 Testing: ONLY metrics from config should be logged")
    print("Config metrics: ['epoch', 'loss', 'accuracy']")
    print("Should NOT see: 'step' in Run history")
    print("=" * 60)
    
    result = train_model()
    print(f"✅ {result}")
    
    print("\n" + "=" * 60)
    print("🎯 Check WandB output above:")
    print("   ✅ SHOULD see: epoch, loss, accuracy")
    print("   ❌ Should NOT see: step") 
    print("📊 Only config-specified metrics should appear!") 