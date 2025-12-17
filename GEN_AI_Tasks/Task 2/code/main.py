from scraper import fetch_trending_product
from seo_keywords import generate_seo_keywords
from blog_generator import generate_blog
import os

def save_blog_md(title, content, keywords):
    os.makedirs("../outputs", exist_ok=True)

    with open("../outputs/blog_post.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(content)
        f.write("\n\n---\n")
        f.write("SEO Keywords:" + ", ".join(keywords))


if __name__ == "__main__":
    product = fetch_trending_product()
    keywords = generate_seo_keywords(product["name"])
    blog = generate_blog(product, keywords)

    save_blog_md(product["name"], blog, keywords)
    print("Blog generated: outputs/blog_post.md")
