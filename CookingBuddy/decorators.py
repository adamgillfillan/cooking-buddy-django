from django.http import HttpResponseRedirect

def require_user_name(view_func):
    def _wrapped_view_func(request, *args, **kwargs): 
        if not request.COOKIES.get('name'):     
            return HttpResponseRedirect('/cooking_buddy/new_user')            
        else:
             return view_func(request, *args, **kwargs)     
    return _wrapped_view_func