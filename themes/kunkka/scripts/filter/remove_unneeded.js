'use strict';

hexo.extend.filter.register('after_generate',function(){
    var theme = hexo.theme.config,
        buttons = theme.buttons,
        github_comment = theme.github_comment,
        disqus = theme.disqus_shortname,
        d_api = theme.disqus_api_key;
    
    if(!disqus || !d_api) {
        hexo.route.remove('js/disqus.js');
    }
    
    if(!github_comment || !github_comment.repo) {
        hexo.route.remove('js/github-comment.js');
    }
    
    if(!buttons.base || !buttons.dropdown) {
        hexo.route.remove('js/buttons.js');
    }
});
