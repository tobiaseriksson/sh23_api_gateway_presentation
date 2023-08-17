
function add_custom_field_to_json(resp) 
    print("- - - - - - - - - - - - - - - add_custom_field_to_json - - - - - - - - - - - - - - - ")    
    local data = resp:data()    
    data:set('currentTime', os.date("%H:%M:%S") )
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
end
