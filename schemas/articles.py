def article_entity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "id": item["id"],
        "title": item["title"],
        "url": item["url"],
        "imageUrl": item["imageUrl"],
        "newsSite": item["newsSite"],
        "summary": item["summary"],
        "publishedAt": item["publishedAt"],
        "updatedAt": item["updatedAt"],
        "featured": item["featured"],
        "launches": item["launches"],
        "events": item["events"]
    }


def articles_entity(entity) -> list:
    return [article_entity(item) for item in entity]
