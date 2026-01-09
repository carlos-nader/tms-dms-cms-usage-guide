-- ========================================================================
-- Template Variable Substitution for Pandoc Markdown to DOCX
-- ========================================================================
--
-- Purpose: Replace template variables (${VERSION}, ${DATE}, etc.) with
--          actual values before Pandoc conversion.
--
-- Supported Variables:
--  ${VERSION}    - Current project version (from version-system-v4-2.md)
--  ${DATE}       - Current date (YYYY-MM-DD format)
--  ${DATETIME}   - Current date and time (YYYY-MM-DD HH:MM:SS format)
--  ${PROJECT}    - Project name (Falcon BMS TMS/DMS/CMS Guide)
--  ${PHASE}      - Current phase (from PROJECT-TRACKING)
--  ${AUTHOR}     - Document author (if available)
--  ${LOCALE}     - System locale/language
--
-- Usage:
--  In your .md files, use:
--    Version: ${VERSION}
--    Date: ${DATE}
--    Project: ${PROJECT}
--
-- This Lua filter replaces these before DOCX generation.
--
-- ========================================================================

-- Import OS module for date/time handling
local os = require('os')

-- ========================================================================
-- VARIABLE CONFIGURATION
-- ========================================================================
-- Define available variables and their sources

local variables = {
    VERSION = os.getenv('FALCON_VERSION') or '0.2.2.0',
    DATE = os.date('%Y-%m-%d'),
    DATETIME = os.date('%Y-%m-%d %H:%M:%S'),
    PROJECT = 'Falcon BMS TMS/DMS/CMS Guide',
    PHASE = os.getenv('FALCON_PHASE') or 'Pre-Publication (0.x.x.x)',
    AUTHOR = os.getenv('FALCON_AUTHOR') or 'Carlos Nader',
    LOCALE = os.getenv('LANG') or 'en_US',
    TIME = os.date('%H:%M:%S'),
    YEAR = os.date('%Y'),
    MONTH = os.date('%B'),  -- Full month name
    DAY = os.date('%d'),
    WEEKDAY = os.date('%A'), -- Full day name
}

-- ========================================================================
-- HELPER FUNCTION: Load variables from environment or files
-- ========================================================================

local function load_variables_from_env()
    -- Try to read version from file if env var not set
    if not os.getenv('FALCON_VERSION') then
        local version_file = io.open('docs/version-system-v4-2.md', 'r')
        if version_file then
            for line in version_file:lines() do
                if line:match('Current Version:') or line:match('v0%.') then
                    local version = line:match('v[0-9]+%.[0-9]+%.[0-9]+%.[0-9]+')
                    if version then
                        variables.VERSION = version
                        break
                    end
                end
            end
            version_file:close()
        end
    end
    
    -- Try to read phase from PROJECT-TRACKING if available
    if not os.getenv('FALCON_PHASE') then
        local tracking_file = io.open('docs/PROJECT-TRACKING-v4-1-2.md', 'r')
        if tracking_file then
            for line in tracking_file:lines() do
                if line:match('Phase') then
                    variables.PHASE = line:match('Phase [0-9%+%-%.%w]+') or variables.PHASE
                    break
                end
            end
            tracking_file:close()
        end
    end
end

-- Load variables from environment/files on startup
load_variables_from_env()

-- ========================================================================
-- FILTER FUNCTION: String Replacement
-- ========================================================================
-- Replaces all template variables in text content

local function replace_variables(text)
    local result = text
    
    for var_name, var_value in pairs(variables) do
        local pattern = '%$%{' .. var_name .. '%}'
        result = result:gsub(pattern, tostring(var_value))
    end
    
    return result
end

-- ========================================================================
-- PANDOC FILTERS FOR VARIABLE SUBSTITUTION
-- ========================================================================

local function process_str(str_elem)
    -- Replace variables in plain text strings
    str_elem.text = replace_variables(str_elem.text)
    return str_elem
end

local function process_code(code_elem)
    -- Replace variables in inline code (optional - usually not needed)
    -- Uncomment if you want variables in code blocks:
    -- code_elem.text = replace_variables(code_elem.text)
    return code_elem
end

local function process_raw_block(raw_elem)
    -- Replace variables in raw blocks (HTML, LaTeX, etc.)
    raw_elem.text = replace_variables(raw_elem.text)
    return raw_elem
end

local function process_raw_inline(raw_elem)
    -- Replace variables in raw inline elements
    raw_elem.text = replace_variables(raw_elem.text)
    return raw_elem
end

-- ========================================================================
-- UTILITY FUNCTION: Print available variables
-- ========================================================================

local function print_available_variables()
    -- For debugging: print all available template variables
    io.stderr:write('\n========================================\n')
    io.stderr:write('Available Template Variables:\n')
    io.stderr:write('========================================\n')
    
    for var_name, var_value in pairs(variables) do
        io.stderr:write(string.format('  ${%-12} = %s\n', var_name, tostring(var_value)))
    end
    
    io.stderr:write('========================================\n\n')
end

-- Uncomment to debug:
-- print_available_variables()

-- ========================================================================
-- RETURN FILTERS TO PANDOC
-- ========================================================================

return {
    Str = process_str,
    Code = process_code,
    RawBlock = process_raw_block,
    RawInline = process_raw_inline,
}

-- ========================================================================
-- END OF TEMPLATE VARIABLE FILTER
-- ========================================================================
