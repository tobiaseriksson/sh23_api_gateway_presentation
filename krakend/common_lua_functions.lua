
function hello_world()
    print("hello world !")
end

function print_router_context_info(context)
    print("- - - - - - - - - - - - - - - Dump some Request info - - - - - - - - - - - - - - - ")    
    print("type: "..type(context))
    print("host: "..context:host())
    print("URL: "..context:url())
    print("Method:"..context:method())
    -- print("path:"..r:path())
    -- print("query:"..r:query())
    local b3traceid = context:headers('X-B3-Traceid')
    if( b3traceid == nil or b3traceid == '' ) then
        print("No B3-TraceId found!")
    else
        print("B3-TraceId = "..b3traceid)
    end
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

function split(str,sep)    
    local tokens={}
    for s in string.gmatch(str, "([^"..sep.."]+)") do
            table.insert(tokens, s)
    end
    return tokens
end

function params(str)    
    local result = {}
    for _,v in pairs(split(str,'&')) do
        -- print("Value = "..v)
        local tokens = split(v,'=')
        result[tokens[1]] = tokens[2]
    end
    return result
end

function param_to_post(req)
    print("Converting query = "..req:query()..' to a POST request')
    local query = req:query();       
    local par = params(query)
    local city = par['city']
    local street = par['street']    
    
    if  city == nil or city == '' or street == nil or street == '' then
        custom_error("Need to specify both city and street as request parameter!", 400)
        return;
    end

    new_body = '{ "city": "'..city..'", "street": "'..street..'" }'    
    req:body(new_body)
    req:method('POST')
    -- req:headers('Content-Type','application/json; charset=UTF-8')
    -- req:headers('Accept','application/json')
    -- req:headers('Content-Length',tostring(string.len(new_body)))
    req:query('')
end