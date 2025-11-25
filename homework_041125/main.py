from fastapi import FastAPI, Depends, Body,Path,HTTPException,status
from sqlalchemy import func, select
import uvicorn
from models import Animals
from settings import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import AnimalModel

app = FastAPI()


@app.get("/animals")
async def get_animals(db: AsyncSession = Depends(get_db)):
    all_animals = await db.scalars(select(Animals))
    return all_animals.all()

@app.get("/animals/{animal_id}")
async def get_id_animals(animal_id: int,db: AsyncSession = Depends(get_db)):
    animal = await db.get(Animals, animal_id)

    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,)
    elif animal.age < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        return animal

@app.post("/animals", response_model=AnimalModel)
async def create_note(
    db: AsyncSession = Depends(get_db),
    animal_data:AnimalModel = Body(),
):
    animal = Animals(name=animal_data.name, age=animal_data.age,adoped=animal_data.adoped)
    db.add(animal)
    await db.commit()
    await db.refresh(animal)
    return animal




if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True, port=5000)