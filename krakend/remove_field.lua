
function remove_unwanted_fields_from_json(resp)    
    -- When the encoding is 'json' then the Data-object contains the JSON structure in a luaTable
    -- Here we can access the content of the json through data:get(key) see example below
    print("- - - - - - - - - - - - - - - remove_unwanted_fields_from_json - - - - - - - - - - - - - - - ")    
    local data = resp:data()    
    data:del('databaseId')    
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end
