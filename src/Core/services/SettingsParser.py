import re
class SettingsParser:
    def __init__(self, settings):
        self.settings = settings

    def parse(self):
        settings = self.settings.split("\n")
        parsed_settings = self.__parse_block(settings)
        return parsed_settings

    def __parse_block(self, lines):
        """Parses a block of key-value pairs into a dictionary."""
        result = {}
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line:
                i += 1
                continue
            # Check if the line is a key-value pair
            match = re.match(r'(\w+) *= *(.+)', line)
            if match:
                key, value = match.groups()
                key = key.strip()
                value = value.strip()

                # Check if the value starts a new block
                if value == '{':
                    # Find where the block ends
                    block_lines = []
                    brace_count = 1
                    i += 1
                    while i < len(lines):
                        line = lines[i].strip()
                        if line == '{':
                            brace_count += 1
                        elif line == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                break
                        block_lines.append(line)
                        i += 1
                    result[key] = self.__parse_block(block_lines)
                # elif value == 'None':
                #     result[key] = None
                else:
                    # Try to convert the value to int if possible, otherwise leave it as a string
                    try:
                        result[key] = int(value)
                    except ValueError:
                        result[key] = value
            i += 1
        return result




