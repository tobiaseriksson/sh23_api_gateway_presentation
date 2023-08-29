
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
        print("No X-B3-TraceId found!")
    else
        print("X-B3-TraceId = "..b3traceid)
    end

    local b3sampled = context:headers('X-B3-Sampled')
    if( b3sampled == nil or b3sampled == '' ) then
        print("No X-B3-Sampled found!")
    else
        print("X-B3-Sampled = "..b3sampled)
    end

    local b3spanId = context:headers('X-B3-SpanId')
    if( b3spanId == nil or b3spanId == '' ) then
        print("No X-B3-SpanId found!")
    else
        print("X-B3-SpanId = "..b3spanId)
    end

    local b3parentSpanId = context:headers('X-B3-ParentSpanId')
    if( b3parentSpanId == nil or b3parentSpanId == '' ) then
        print("No X-B3-ParentSpanId found!")
    else
        print("X-B3-ParentSpanId = "..b3parentSpanId)
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
