#!/usr/bin/env python3
"""
Remove Enterprise module references from OCB base data files.
This script removes entire <record> blocks that reference Enterprise-only module categories.
"""

import re
import sys
from pathlib import Path

def cleanup_ir_module_module_xml(file_path):
    """Remove records that reference Enterprise module categories."""
    
    print(f"🔧 Processing {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_length = len(content)
    
    # Enterprise category patterns to remove
    enterprise_categories = [
        'module_category_services_timesheets',
        'module_category_manufacturing', 
        'module_category_marketing',
        'module_category_project',
        'module_category_services_delivery',
        'module_category_human_resources_attendance',
        'module_category_human_resources_expenses',
        'module_category_human_resources_fleet',
    ]
    
    # Remove entire <record> blocks that contain any Enterprise category reference
    for category in enterprise_categories:
        # Pattern matches: <record ...> ... category_id ref="base.CATEGORY" ... </record>
        pattern = rf'<record[^>]*>.*?ref="base\.{category}".*?</record>'
        matches = re.findall(pattern, content, flags=re.DOTALL)
        
        if matches:
            print(f"  ℹ️  Removing {len(matches)} record(s) referencing {category}")
            content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    # Clean up extra blank lines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    bytes_removed = original_length - len(content)
    print(f"✅ Removed {bytes_removed} bytes from {file_path}")
    
    return bytes_removed > 0

if __name__ == '__main__':
    base_path = Path('/opt/odoo/src/odoo/odoo/addons/base/data')
    xml_file = base_path / 'ir_module_module.xml'
    
    if not xml_file.exists():
        print(f"❌ File not found: {xml_file}")
        sys.exit(1)
    
    success = cleanup_ir_module_module_xml(xml_file)
    
    if success:
        print("✅ Enterprise module cleanup completed successfully")
        sys.exit(0)
    else:
        print("⚠️  No changes made - file may already be clean")
        sys.exit(0)
