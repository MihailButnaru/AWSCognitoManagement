# Copyright 2019 by Mihail Butnaru
# All rights reserved.
from flask import request, jsonify
from flask_restplus import Resource
from api.models.scopes import namespace as ns 
from api.models.scopes import scope_model
from api.wrappers import scope_manager

@ns.route('/', resource_class_kwargs={'scope_manager': scope_manager})
class ScopesList(Resource):
    """
    Shows a list of scopes that were created in the user pool, name and description
    of the scope is displayed too in order to understand more about the scope.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scope_manager = kwargs['scope_manager']

    @ns.response(200, 'Success')
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def get(self):
        """
        Lists all the scopes from the defined user pool, the configuration is in 
        the config file.
        """
        return self.scope_manager.get_scopes(), 200


    @ns.expect(scope_model)
    @ns.marshal_with(scope_model, code=201)
    @ns.response(404, 'Validation Error')
    @ns.response(500, 'Internal Server Error')
    def post(self):
        """
        """
        pass