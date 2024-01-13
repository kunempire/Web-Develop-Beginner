This is the UI based on Web (front-end) of the final project in *Data Security and Privacy Protection*.

## Why Web

1. **Project Requirement**: To submit, the application needs to be packaged into a Docker, which does not have a desktop application window, only command lines. Therefore, by web developing, Docker can be used as a server to serve an application with interactive interfaces.

2. **Web Advantages**: Technologies of Web developing are mature and systematic, with a wide range of beautiful and user-friendly frameworks and templates available for rapid application development.

## Structure

```bash
.
├── fuction # app functions to implement
│   ├── AIGC_image_detect
│   ├── AIGC_text_detect
│   └── picture_tampering_detect
├── static # static resources required
│   ├── css
│   ├── fonts
│   ├── images
│   ├── js
│   └── resource # files
├── templates # html templates
│   ├── about.html
│   ├── blog-single.html
│   ├── home.html
│   ├── image-distinguish.html
│   ├── tampering-detect.html
│   └── text-distinguish.html
├── web-page_org.zip # original web page template
├── utils.py # functions
└── main.py # application entrance
```

## Quick Start

This Web application is based on `Python Flask`, requiring `pip install flask` first. As for other packages needed, you can check in `utils.py` or wait for `error` to install.

Just run `main.py` directly. If the port is occupied, change it.

## Attention

1. This is only a template without real functions.

2. Due to a development period of only 3 days, as well as being the first attempt at web development, there may be many bugs, inconsistencies, and disharmonies in the code. For reference only, your understanding is appreciated.
