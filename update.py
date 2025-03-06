import requests

API_URL = 'https://mewis.me/api/latest'
MARKDOWN_FILE_PATH = 'README.md'

def fetch_blog_posts():
    response = requests.get(API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def generate_markdown_content(json):
    updated_at = json['updated_at']
    return f"\n#### ⏲️ &nbsp;Updated At: {updated_at}\n\n{'\n'.join([post['markdown'] for post in json['posts']])}"

def update_markdown_file(file_path, new_content):
    with open(file_path, 'r', encoding='utf-8') as file:
        markdown = file.read()
    start_tag = '<!-- start-blog-posts -->'
    end_tag = '<!-- end-blog-posts -->'
    start_index = markdown.find(start_tag)
    end_index = markdown.find(end_tag, start_index)
    if start_index == -1 or end_index == -1:
        raise ValueError('Start or end tag not found in the markdown file')
    before_start = markdown[:start_index + len(start_tag)]
    after_end = markdown[end_index:]
    new_markdown = f"{before_start}\n{new_content}\n{after_end}"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_markdown)

def main():
    json = fetch_blog_posts()
    new_content = generate_markdown_content(json)
    update_markdown_file(MARKDOWN_FILE_PATH, new_content)

if __name__ == '__main__':
    main()
