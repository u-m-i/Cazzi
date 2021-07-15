"""Cazzi middlewares stack."""

# Django 

from django.shortcuts import redirect, render
from django.urls import reverse

# Exceptions


class ProfileCompletionMiddleWare:
    """ Verify the completness of the user´s profile

    Ensure the picture and biography existing.
    """

    def __init__(self, get_response):
        """ Middleware initialization
        """
        self.get_response = get_response


    def __call__ (self,request):
        """Action each request and response"""
        
        try:

            if not request.user.is_anonymous:

                if not request.user.is_staff:

                    profile = request.user.profile

                    if not profile.picture or not profile.biography:

                        if request.path not in [reverse("update_profile "), reverse("logout")]:

                            return redirect("update_profile")
            
            
            response =  self.get_response(request)

            return response
            
        except:

            return reverse("signup")


                
        
