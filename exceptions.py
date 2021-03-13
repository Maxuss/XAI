# ВНИМАНИЕ!
# Какое-либо изменение данных этого файла сделает так, что вы не
# сможете получать валидные предупреждения и ошибки!!!
# Изменяйте на свой собственный риск!

# main class for errors
class Error(Exception):
    pass

# errors related to files
class FileErrors(Error):
    # appears if cant find ./data files
    class CantFindDataFiles(Error):
        pass

    # appears if no files in ./ref/lootgen
    class CantGenerateLoot(Error):
        pass
    
    # appears when file is corrupted
    class FileCorruptedError(Error):
        pass
    
    # appears when you modify files without permissions
    class IllegalFileManipulations(Error):
        pass

    # unknown file error
    class UnknownFileError(Error):
        pass

# errors related to JSON parsing
class JSONErrors(Error):
    # appears if cant parse inventory player data
    class CantParseInventoryData(Error):
        pass
    
    # appears if cant find referrers
    class CantFindReferrers(Error):
        pass
    
    # appears if cant parse any other json
    class CantParseMainJSON(Error):
        pass

    # unknown JSON error
    class UnknownJSONError(Error):
        pass

# all fatals are really dangerous exceptions that have to be fixed ASAP
class Fatals(Error):
    
    # appears when cant find playerdata files
    class CantFindPlayerDataFiles(Error):
        pass

    # unknown errors. SHOULD BE OPENED ISSUES IN GITHUB
    class UnknownFatalException(Error):
        pass