import wmi, getpass, platform, os

class c:
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    R = '\033[91m' #RED
    W = '\033[0m' #RESET COLOR
    P = '\033[35m' # PURPLE
    B = '\033[96m' # CYAN

computer = wmi.WMI()
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
user = getpass.getuser()

windows_version = platform.version().split('.')
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576

def COLORED():
    if platform.system().lower().startswith('win'):
    
        # please uncomment the below line if you wan't to clear the console before this is showing up
        # os.system("cls")
        
        
        print(f"""
    {c.G}████████████████████{c.W}    {c.B}OS: {c.B}{c.W}{c.Y}{os_info.Caption} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░░░░░░░░░░░░░░░{c.P}{c.G}█{c.G}{c.W}    {c.B}Build: {c.B}{c.W}{c.Y}{os_info.BuildNumber} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░{c.P}{c.Y}▄▀▄▀▄▀▄▀▄▀▄▀▄▀{c.Y}{c.P}░░{c.P}{c.G}█{c.G}{c.W}    {c.B}OS Architechture: {c.B}{c.W} {c.Y} {os_info.OSArchitecture} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░░░░░░░░░{c.P}{c.Y}▄▀▄▀{c.Y}{c.P}░░{c.P}{c.G}█{c.G}{c.W}    {c.B}CPU: {c.B}{c.W}{c.Y}{proc_info.Name} {c.Y}{c.W}
    {c.G}█████████{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}█{c.G}{c.W}    {c.B}CPU Desc.: {c.B}{c.W}{c.Y}{proc_info.Description} {c.Y}{c.W}
    {c.G}███████{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}███{c.G}{c.W}    {c.B}GPU: {c.B}{c.W}{c.Y}{gpu_info.VideoProcessor} {c.Y}{c.W}
    {c.G}█████{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}█████{c.G}{c.W}    {c.B}GPU Driver Version: {c.B}{c.W}{c.Y}{gpu_info.DriverVersion} {c.Y}{c.W}
    {c.G}███{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}███████{c.G}{c.W}    {c.B}System Name: {c.B}{c.W}{c.Y}{proc_info.SystemName} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}█████████{c.G}{c.W}    {c.B}System RAM: {c.B}{c.W}{c.Y}{system_ram} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░{c.P}{c.Y}▄▀▄▀{c.Y}{c.P}░░░░░░░░░░░░{c.P}{c.G}█{c.G}{c.W}    {c.B}Boot Drive: {c.B}{c.W}{c.Y}{os_info.BootDevice} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░{c.P}{c.Y}▄▀▄▀▄▀▄▀▄▀▄▀▄▀{c.Y}{c.P}░░{c.P}{c.G}█{c.G}{c.W}    {c.B}UserName: {c.B}{c.W}{c.Y}{user} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░░░░░░░░░░░░░░░{c.P}{c.G}█{c.W}    {c.R}▀█ █▀▀ ▄▀█ █▀▀ █▀▀ █▀█{c.R}{c.W}
    {c.G}████████████████████{c.G}{c.W}    {c.R}█▄ ██▄ █▀█ █▄▄ ██▄ █▀▄{c.R}{c.W}
        """ )
    else:
    
        # please uncomment the below line if you wan't to clear the console before this is showing up
        # os.system("clear")
        
        
        print(f"""
    {c.G}████████████████████{c.W}    {c.B}OS: {c.B}{c.W}{c.Y}{os_info.Caption} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░░░░░░░░░░░░░░░{c.P}{c.G}█{c.G}{c.W}    {c.B}Build: {c.B}{c.W}{c.Y}{os_info.BuildNumber} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░{c.P}{c.Y}▄▀▄▀▄▀▄▀▄▀▄▀▄▀{c.Y}{c.P}░░{c.P}{c.G}█{c.G}{c.W}    {c.B}OS Architechture: {c.B}{c.W} {c.Y} {os_info.OSArchitecture} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░░░░░░░░░{c.P}{c.Y}▄▀▄▀{c.Y}{c.P}░░{c.P}{c.G}█{c.G}{c.W}    {c.B}CPU: {c.B}{c.W}{c.Y}{proc_info.Name} {c.Y}{c.W}
    {c.G}█████████{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}█{c.G}{c.W}    {c.B}CPU Desc.: {c.B}{c.W}{c.Y}{proc_info.Description} {c.Y}{c.W}
    {c.G}███████{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}███{c.G}{c.W}    {c.B}GPU: {c.B}{c.W}{c.Y}{gpu_info.VideoProcessor} {c.Y}{c.W}
    {c.G}█████{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}█████{c.G}{c.W}    {c.B}GPU Driver Version: {c.B}{c.W}{c.Y}{gpu_info.DriverVersion} {c.Y}{c.W}
    {c.G}███{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}███████{c.G}{c.W}    {c.B}System Name: {c.B}{c.W}{c.Y}{proc_info.SystemName} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░{c.P}{c.Y}▄▀{c.Y}{c.P}░░░░{c.P}{c.G}█████████{c.G}{c.W}    {c.B}System RAM: {c.B}{c.W}{c.Y}{system_ram} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░{c.P}{c.Y}▄▀▄▀{c.Y}{c.P}░░░░░░░░░░░░{c.P}{c.G}█{c.G}{c.W}    {c.B}Boot Drive: {c.B}{c.W}{c.Y}{os_info.BootDevice} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░{c.P}{c.Y}▄▀▄▀▄▀▄▀▄▀▄▀▄▀{c.Y}{c.P}░░{c.P}{c.G}█{c.G}{c.W}    {c.B}UserName: {c.B}{c.W}{c.Y}{user} {c.Y}{c.W}
    {c.G}█{c.G}{c.P}░░░░░░░░░░░░░░░░░░{c.P}{c.G}█{c.W}    {c.R}▀█ █▀▀ ▄▀█ █▀▀ █▀▀ █▀█{c.R}{c.W}
    {c.G}████████████████████{c.G}{c.W}    {c.R}█▄ ██▄ █▀█ █▄▄ ██▄ █▀▄{c.R}{c.W}
        """ )

def NOT_COLORED():
    if platform.system().lower().startswith('win'):
        os.system("cls")
        print(f"""
    ████████████████████    OS: {os_info.Caption}
    █░░░░░░░░░░░░░░░░░░█    Build: {os_info.BuildNumber}
    █░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█    OS Architechture: {os_info.OSArchitecture}
    █░░░░░░░░░░░░▄▀▄▀░░█    CPU: {proc_info.Name}
    █████████░░░░▄▀░░░░█    CPU Desc.: {proc_info.Description} 
    ███████░░░░▄▀░░░░███    GPU: {gpu_info.VideoProcessor}
    █████░░░░▄▀░░░░█████    GPU Driver Version: {gpu_info.DriverVersion}
    ███░░░░▄▀░░░░███████    System Name: {proc_info.SystemName}
    █░░░░▄▀░░░░█████████    System RAM: {system_ram}
    █░░▄▀▄▀░░░░░░░░░░░░█    Boot Drive: {os_info.BootDevice}
    █░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█    UserName: {user}
    █░░░░░░░░░░░░░░░░░░█    ▀█ █▀▀ ▄▀█ █▀▀ █▀▀ █▀█
    ████████████████████    █▄ ██▄ █▀█ █▄▄ ██▄ █▀▄
        """ )
    else:
        os.system("clear")
        print(f"""
    ████████████████████    OS: {os_info.Caption}
    █░░░░░░░░░░░░░░░░░░█    Build: {os_info.BuildNumber}
    █░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█    OS Architechture: {os_info.OSArchitecture}
    █░░░░░░░░░░░░▄▀▄▀░░█    CPU: {proc_info.Name}
    █████████░░░░▄▀░░░░█    CPU Desc.: {proc_info.Description} 
    ███████░░░░▄▀░░░░███    GPU: {gpu_info.VideoProcessor}
    █████░░░░▄▀░░░░█████    GPU Driver Version: {gpu_info.DriverVersion}
    ███░░░░▄▀░░░░███████    System Name: {proc_info.SystemName}
    █░░░░▄▀░░░░█████████    System RAM: {system_ram}
    █░░▄▀▄▀░░░░░░░░░░░░█    Boot Drive: {os_info.BootDevice}
    █░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█    UserName: {user}
    █░░░░░░░░░░░░░░░░░░█    ▀█ █▀▀ ▄▀█ █▀▀ █▀▀ █▀█
    ████████████████████    █▄ ██▄ █▀█ █▄▄ ██▄ █▀▄
        """ )

COLORED()
# NOT_COLORED()