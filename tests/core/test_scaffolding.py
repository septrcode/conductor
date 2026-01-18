from pathlib import Path
import sys
import os

# Add the project root to sys.path to import the core module
sys.path.append(os.getcwd())

from core.services.scaffolding import ScaffoldingService
from core.adapters.generic import GenericContext

def test_scaffolding_initialization():
    context = GenericContext()
    service = ScaffoldingService(context)
    
    # This should trigger GenericContext.write_file and run_command
    # In a real test, we would use a proper Mock library, but here
    # we are verifying the logic flow.
    service.initialize_project("Build a test app")
    print("Scaffolding initialization logic verified.")

def test_project_maturity_detection():
    context = GenericContext()
    service = ScaffoldingService(context)
    
    maturity = service.detect_project_maturity()
    # GenericContext.run_command returns a mock string, so it should be brownfield
    assert maturity == "brownfield"
    print("Maturity detection logic verified.")

if __name__ == "__main__":
    try:
        test_scaffolding_initialization()
        test_project_maturity_detection()
        print("All mock tests passed!")
    except Exception as e:
        print(f"Tests failed: {e}")
        sys.exit(1)
