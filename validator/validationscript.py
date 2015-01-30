__author__ = 'stephane'

''' Main module to run the validation script which generates
'   the excel files containing the results of the comparison
'   between successive iterations of the skill cartridge '''
import argparse
import manualtagsimport
import temisxmlparser
import csvparser
import excelgenerator

def main():
    parser = argparse.ArgumentParser(
        description="Validate the document classification produced by Temis Luxid(c).\n"
                    "Typical execution sequence would be m => [t => c => e]*x.\n"
                    "First extract the manual annotations to produce a baseline: -m .\n"
                    "Next, extract the annotations produced in xml format by temis and convert to csv: -t\n"
                    "Next, parse the csv files and compare to the manual annotations: -c\n"
                    "Finally, generate an excel file: -e.\n"
                    "Repeat the last 3 steps as many times as required.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--csv", action="store_true", help="run csvparser script")
    group.add_argument("-m", "--manualtags", action="store_true", help="run manualtagsimport script")
    group.add_argument("-t", "--temisxml", action="store_true", help="run temisxmlparser script")
    group.add_argument("-e", "--excel", action="store_true", help="run excelgenerator script")
    args = parser.parse_args()
    if args.csv:
        print "Generating validation csv file."
        csvparser.main()
    elif args.manualtags:
        print "Importing manual tags."
        manualtagsimport.main()
    elif args.temisxml:
        print "Extracting temis annotations."
        temisxmlparser.main()
    elif args.excel:
        print "Generating Excel spreadsheet."
        excelgenerator.main()


if __name__ == '__main__':
    main()