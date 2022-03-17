from engine.wifux_engine import WifuxEngine

while True:
    command = input("-> ")
    WifuxEngine.run(command)
