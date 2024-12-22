# OrangeMarket
Second-hand item market Web site

# 트러블슈팅

1. 게시글을 수정할 때 이미지파일이 수정되지 않는 문제
 -  enctype="multipart/form-data" 가 update.html의 폼에 선언되어있지 않았음

2. TemplateSyntaxError at /articles/11/
Invalid block tag on line 10: 'static', expected 'endif'. Did you forget to register or load this tag?
- html 파일에 {% load static %} 이이 선언되어있지 않았음음