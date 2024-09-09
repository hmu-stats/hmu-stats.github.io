Span = function (el)
    -- store the attributes for color and highlight
    color = el.attributes['color']
    highlight = el.attributes['highlight']
    
    -- create a function to check for emptiness
    local function isempty(s)
      return s == nil or s == ''
    end
    
    if FORMAT:match 'latex' then    
      -- use \hl to highlight stuff with {highlight = "some-color"}.
      -- for LaTeX reasons, highlighting should come before font coloring
      if not isempty(highlight) then
        -- remove highlight attributes
        el.attributes['highlight'] = nil
        -- encapsulate in latex code
        table.insert(
          el.content, 1,
          pandoc.RawInline('latex', '\\sethlcolor{'..highlight..'}\\hl{')
        )
        table.insert(
          el.content,
          pandoc.RawInline('latex', '}')
        )
      end
      
      -- use \textcolor to color text with {color = "some-color"}
      if not isempty(color) then
        -- remove color attributes
        el.attributes['color'] = nil
        -- encapsulate in latex code
        table.insert(
          el.content, 1,
          pandoc.RawInline('latex', '\\textcolor{'..color..'}{')
        )
        table.insert(
          el.content,
          pandoc.RawInline('latex', '}')
        )
      end
    
      return el.content 
    end
    
    if FORMAT:match 'html' then
      style_attributes = ''
      
      if not isempty(highlight) then
        -- remove highlight attributes
        el.attributes['highlight'] = nil
        -- use style attribute instead
        style_attributes = 'background-color: ' .. highlight .. ';'
      end
      
      if not isempty(color) then
        -- remove color attributes
        el.attributes['color'] = nil
        -- use style attribute instead
        style_attributes = style_attributes .. ' color: ' .. color .. ' !important;'
      end
      
      if not isempty(style_attributes) then
        el.attributes['style'] = style_attributes
      end
      
      -- return entire span content
      return el
    end

    if FORMAT:match 'revealjs' then
      style_attributes = ''
      
      if not isempty(highlight) then
        -- remove highlight attributes
        el.attributes['highlight'] = nil
        -- use style attribute instead
        style_attributes = 'background-color: ' .. highlight .. ';'
      end
      
      if not isempty(color) then
        -- remove color attributes
        el.attributes['color'] = nil
        -- use style attribute instead
        style_attributes = style_attributes .. ' color: ' .. color .. ' !important;'
      end
      
      if not isempty(style_attributes) then
        el.attributes['style'] = style_attributes
      end
      
      -- return entire span content
      return el
    end    
    
  end
