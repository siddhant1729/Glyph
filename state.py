from typing import List, TypedDict, Optional

class GlyphState(TypedDict):
    image_path: str                 # Path to your diagram
    diagram_description: Optional[str] 
    tech_stack: List[str]           # e.g., ["FastAPI", "C++"]
    retrieved_snippets: List[str]   # Code found in your library
    generated_code: Optional[str]   
    is_validated: bool              # For self-correction loops
    iteration_count: int