define({ "api": [
  {
    "type": "post",
    "url": "/user/create/",
    "title": "",
    "name": "Create_User",
    "group": "User",
    "description": "<p>Create a user</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>user's name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>user's address</p>"
          },
          {
            "group": "Parameter",
            "type": "Integer",
            "optional": false,
            "field": "age",
            "description": "<p>user's age</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"id\" : <generated id>\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "endpoint/create_user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/user/view/{id}",
    "title": "",
    "name": "Create_User",
    "group": "User",
    "description": "<p>View Specific User</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n  \"id\" : <generated id>,\n  \"name\" : <user's name>,\n  \"address\" : <user's address>,\n  \"age\" : \"<user's age>\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "endpoint/view_user.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/user/delete/{id}",
    "title": "",
    "name": "Delete",
    "group": "User",
    "description": "<p>Delete User by ID</p>",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "endpoint/delete_user.py",
    "groupTitle": "User"
  },
  {
    "type": "put",
    "url": "/user/create/",
    "title": "",
    "name": "Update_User",
    "group": "User",
    "description": "<p>Update User Fields</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>user's name</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "address",
            "description": "<p>user's address</p>"
          },
          {
            "group": "Parameter",
            "type": "Integer",
            "optional": false,
            "field": "age",
            "description": "<p>user's age</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "endpoint/update_user.py",
    "groupTitle": "User"
  }
] });
