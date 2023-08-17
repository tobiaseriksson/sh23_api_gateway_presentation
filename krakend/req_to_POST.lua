
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
    req:headers('Content-type','application/json; charset=utf-8')
    req:query('')
end