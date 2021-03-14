# frameworks
from forest._importable import LazyImport


fastapi = LazyImport("import fastapi")
FastAPI = LazyImport("from fastapi import FastAPI")
pydantic = LazyImport("import pydantic")
tornado = LazyImport("import tornado")
sanic = LazyImport("import sanic")
Sanic = LazyImport("from sanic import Sanic")