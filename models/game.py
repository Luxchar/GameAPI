import uuid
from typing import Optional
from pydantic import BaseModel, Field
        
class Game(BaseModel):
    """ Game model """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="id")
    Title: Optional[str] = Field(alias="Title")
    Release_Date: Optional[str] = Field(alias="Release Date")
    Developer: Optional[str] = Field(alias="Developer")
    Publisher: Optional[str] = Field(alias="Publisher")
    Genres: Optional[str] = Field(alias="Genres")
    Genres_Splitted: Optional[str] = Field(alias="Genres Splitted")
    User_Score: Optional[float] = Field(alias="User Score", default=None)
    User_Ratings_Count: Optional[int] = Field(alias="User Ratings Count", default=None)
    Platforms_Info: Optional[str] = Field(alias="Platforms Info")
    
    class Config:
        """ Pydantic configuration """
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "Title": "The Legend of Zelda: Breath of the Wild",
                "Release Date": "2017-03-03",
                "Developer": "Nintendo",
                "Publisher": "Nintendo",
                "Genres": "Action-Adventure",
                "Genres Splitted": "Action, Adventure",
                "User Score": 4.8,
                "User Ratings Count": 100,
                "Platforms Info": "Nintendo Switch"
            }
        }