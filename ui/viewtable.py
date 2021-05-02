class ViewTable(object):
    view_mode = 'white'
    free_cell_symbol = 'X'

    @staticmethod
    def view():
        print('\t\t\t\t  BLACK\t\t\t')
        print('\t*\t*\t*\t*\t*\t*\t*\t*')
        print('1\tR\tN\tB\tQ\tK\tB\tN\tR')
        print('2\tP\tP\tP\tP\tP\tP\tP\tP')
        print('3\tX\tX\tX\tX\tX\tX\tX\tX')
        print('4\tX\tX\tX\tX\tX\tX\tX\tX')
        print('5\tX\tX\tX\tX\tX\tX\tX\tX')
        print('6\tX\tX\tX\tX\tX\tX\tX\tX')
        print('7\tP\tP\tP\tP\tP\tP\tP\tP')
        print('8\tR\tN\tB\tK\tQ\tB\tN\tR')
        print('\t*\t*\t*\t*\t*\t*\t*\t*')
        print('\tA\tB\tC\tD\tE\tF\tG\tH')
        print('\t\t\t\t WHITE\t\t\t')


ViewTable.view()
