class TableLayout:
    """Represents the graphical layout of a generic table.

    attributes: fields_names: list of string
                fields_values: list of string
                fields_widths: list of int
                line_chars: string <= contains the characters for drawing outlines
    """
    line_chars = "╔╗╚╝═║╦╩╠╣╬"
    #             012345678910

    def __init__(self, fields_names_=('Numbers', 'Ruota', 'Type'),
                 fields_values_=('11 12 13 14 15 16 17 18 19 20', 'Palermo', 'Quaterna')):
        self.set_fields_names(fields_names_)
        self.set_fields_values(fields_values_)
        self.set_fields_widths()

    def __str__(self):
        num_fields = len(self.fields_names)
        c = self.line_chars
        width = self.fields_widths
        first_infix = ''
        middle_infix = ''
        last_infix = ''
        text_infix_01 = ''
        text_infix_02 = ''
        for i in range(num_fields-1):
            first_infix  += c[4] * width[i] + c[6]
            middle_infix += c[4] * width[i] + c[10]
            last_infix   += c[4] * width[i] + c[7]
        first_line  = c[0] + first_infix   + c[4] * width[2] + c[1]
        middle_line = c[8] + middle_infix  + c[4] * width[2] + c[9]
        last_line   = c[2] + last_infix    + c[4] * width[2] + c[3]

        for i in range(num_fields):
            text_infix_01 += '{:^{w}}'.format(str(self.fields_names[i]), w=width[i]) + c[5]
            text_infix_02 += '{:^{w}}'.format(str(self.fields_values[i]), w=width[i]) + c[5]
        text_line_01   = c[5] + text_infix_01
        text_line_02   = c[5] + text_infix_02

        return first_line + '\n' + text_line_01 + '\n' + middle_line + '\n' + text_line_02 + '\n' + last_line

    def set_fields_names(self, fields_names_):
        self.fields_names = fields_names_

    def set_fields_values(self, fields_values_):
        self.fields_values = fields_values_

    def set_fields_widths(self):
        self.fields_widths = [max(len(self.fields_names[i]), len(self.fields_values[i])) + 2
                              for i in range(len(self.fields_names))]


if __name__ == '__main__':
    fields_names = ('Numbers', 'Ruota', 'Type')
    fields_values = ('11 12 13 14 15 16 17 18 19 20', 'Palermo', 'Quaterna')
    table_01 = TableLayout(fields_names, fields_values)
    print(table_01)
