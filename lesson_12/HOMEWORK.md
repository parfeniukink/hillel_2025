Using the example from the lesson. Take the frontend and the backend and implement interaction asynchronously. Use `httpx.AsyncClient` and `async def article_idea()` async function to provide ASYNC API.

`generate-article` function must be refactored to the `class ArticleGenerationService` to implement next abstraction:

```python
class GenerationService(abc.ABC):
    @abc.abstractmethod
    async def generate_random_article_idea(): ...

    @abc.abstractmethod
    async def generate_technical_guide(): ...

    @abc.abstractmethod
    async def generate_fiction(): ...
```

The `GenerationService` just represents the abstraction of YOUR concrete service. Implement a bit more logic to generate some articles. You can try connect to **OpenAI API** to send PROMPT and get the article idea.
This is optional, so you can mimic that behavior by generating random strings.

Homework must include backend and frontend. You can try with frontend styles and template if you want.
