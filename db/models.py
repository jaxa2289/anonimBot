import asyncio

from sqlalchemy import String, DECIMAL, select, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from db import Base, db
from db.utils import CreatedModel


class User(CreatedModel):
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    chat_id: Mapped[int] = mapped_column(BigInteger,unique=True)
    status: Mapped[bool]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Juftlar(CreatedModel):
    chat_id_1: Mapped[int] = mapped_column(BigInteger)
    chat_id_2: Mapped[int] = mapped_column(BigInteger)
    status: Mapped[bool]


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Customer(CreatedModel):
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
#     user: Mapped['User'] = relationship("User", back_populates="customers")
#     posts: Mapped[list['Post']] = relationship("Post", back_populates="customer")
#
#
# class Post(CreatedModel):
#     title: Mapped[str] = mapped_column(String(255))
#     description: Mapped[str] = mapped_column(String(255))
#     file: Mapped[str] = mapped_column(String(255))
#     deadline: Mapped[int]
#     status: Mapped[str] = mapped_column(String(55))
#     customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id", ondelete="CASCADE"), nullable=True)
#     customer: Mapped['Customer'] = relationship("Customer", back_populates="posts")
#
# class Subjob(CreatedModel):
#     name: Mapped[str] = mapped_column(String(255))
#     job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id", ondelete="CASCADE"), nullable=True)
#     job: Mapped['Job'] = relationship("Job", back_populates="subjobs")
#
# class Job(CreatedModel):
#     name: Mapped[str] = mapped_column(String(255))
#     subjobs: Mapped[list['Subjob']] = relationship("Subjob", back_populates="job")
#
# class Employee(CreatedModel):
#     experience: Mapped[str] = mapped_column(String(255))
#     linkedin: Mapped[str] = mapped_column(String(255))
#     description: Mapped[str] = mapped_column(String(255))
#     rating: Mapped[str] = mapped_column(String(255))
#     cv: Mapped[str] = mapped_column(String(255))
#     user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
#     user: Mapped['User'] = relationship("User", back_populates="employees")
#
# class SubjobEmployee(CreatedModel):
#     employee_id: Mapped[int] = mapped_column(ForeignKey("employees.id", ondelete="CASCADE"), nullable=True)
#     subjob_id: Mapped[int] = mapped_column(ForeignKey("subjobs.id", ondelete="CASCADE"), nullable=True)
#
#
# class PostSubjob(CreatedModel):
#     subjob_id: Mapped[int] = mapped_column(ForeignKey("subjobs.id", ondelete="CASCADE"), nullable=True)
#     post_id: Mapped[int] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=True)



metadata = Base.metadata



