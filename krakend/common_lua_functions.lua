
function hello_world()
    print("hello world !")
end

function print_request_info(r)
    print("- - - - - - - - - - - - - - - Dump some Request info - - - - - - - - - - - - - - - ")    
    print(type(r))
    print("URL: "..r:url())
    print("Method:"..r:method())
    print("path:"..r:path())
    print("query:"..r:query())
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
end

function print_all_data_fields(resp)
    print("- - - - - - - - - - - - - - - Dump Data Object - - - - - - - - - - - - - - - ")    
    local data = resp:data()
    local keys = data:keys()
    local stop = keys:len() - 1
    print("These are the Keys")
    for idx=0,stop do
        print(tostring(idx).." : "..keys:get(idx))
    end
    print("These are the Keys and Values")
    for idx=0,stop do
        print(keys:get(idx).." = "..data:get(keys:get(idx)))        
    end
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end

function remove_unwanted_fields_from_json(resp)    
    -- When the encoding is 'json' then the Data-object contains the JSON structure in a luaTable
    -- Here we can access the content of the json through data:get(key) see example below
    print("- - - - - - - - - - - - - - - remove_unwanted_fields_from_json - - - - - - - - - - - - - - - ")    
    local data = resp:data()    
    data:del('databaseId')    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end

function replace_body_content(resp)
    -- When the ecoding is set to 'string' then the Data-object contains only ONE key 'content'
    -- And it is just a test string that we can modify as we like
    print("- - - - - - - - - - - - - - - replace_body_content - - - - - - - - - - - - - - - ")    
    local data = resp:data()    
    data:set('content','{ "messsage": "now the body has changed!" }' )
    -- ocal keys = data:keys()
    -- data:set(keys:get(0), '{ "messsage": "body has changed!"}')
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end

function set_content_type_to_json(resp)
    print("- - - - - - - - - - - - - - - set_content_type_to_json - - - - - - - - - - - - - - - ")    
    resp:headers("Content-Type","application/json")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end 

function add_custom_field_to_json(resp) 
    print("- - - - - - - - - - - - - - - add_custom_field_to_json - - - - - - - - - - - - - - - ")    
    local data = resp:data()    
    data:set('currentTime', os.date("%H:%M:%S") )
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end

