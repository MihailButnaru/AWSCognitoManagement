# Copyright 2019 by Mihail Butnaru
# All rights reserved.

class UserSerializer:
    """
    UserSerializer format to the model list of the API Json.
    """ 
    def serialize(self, users):
        """
        Serializer
            Args:
                users (list) : list of users
        """
        if isinstance(users, list):
            attributes = []
            for user in users:
                content = {}
                content['username'] = user['Username']
                for attr in user['Attributes']:
                    if attr['Name'] == 'custom:firstname':
                        content['firstname'] = attr['Value']
                    elif attr['Name'] == 'custom:surname':
                        content['surname'] = attr['Value']
                    elif attr['Name'] == 'email':
                        content['email'] = attr['Value']
                attributes.append(content)
            return attributes
        else:
            content = {}
            content['username'] = users['Username']
            for attr in users['UserAttributes']:
                if attr['Name'] == 'custom:firstname':
                    content['firstname'] = attr['Value']
                elif attr['Name'] == 'custom:surname':
                    content['surname'] = attr['Value']
                elif attr['Name'] == 'email':
                    content['email'] = attr['Value']
            return content
        
