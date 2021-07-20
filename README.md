# Sphinx Docx 文档项目

## 安装依赖
```
安装 Sphinx
pip install sphinx

安装 Read the Docs 主题
pip install sphinx_rtd_theme

安装 Sphinx Markdown 扩展
pip install recommonmark
```

## 初始化
```
创建 docs 目录

cd docs
初始化
sphinx-quickstart
```
### 选项配置参考：
```
> Separate source and build directories (y/n) [n]: y
> Name prefix for templates and static dir [_]:
> Project name: imgkernel
> Author name(s): ken
> Project release []: 0.1.0
> Project language [en]: zh_CN
> Source file suffix [.rst]:
> Name of your master document (without suffix) [index]:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]:
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]:
```
## 更改主题
编辑文档配置文件 docs/source/conf.py。默认主题是 alabaster，将其改为 sphinx_rtd_theme。
```
html_theme = 'sphinx_rtd_theme'
```

> 补充：如需支持 markdown ，添加 recommonmark 扩展到 extensions 配置列表中:
```
extensions = [
    'otherextension',
    '...' ,
    'recommonmark',
]
```

## 生成 html
```
make html
```

## 生成 PDF
```
使用 markdown 模块
安装：
pip install markdown

再通过 chrome 浏览器将网页转成 pdf
```