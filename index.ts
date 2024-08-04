const file = Bun.file('README.md');
const content = await file.text();

content.replace(/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z/, new Date().toISOString());

await Bun.write('README.md', content);