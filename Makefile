server:
	hexo clean && hexo g && hexo server --draft
deploy:
	hexo clean && hexo g && hexo deploy 
