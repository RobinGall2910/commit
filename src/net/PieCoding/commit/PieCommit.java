package net.PieCoding.commit
// Welcome to PieCommit where half of the code is fake!!!±! ahahhahahah

import me.rsajeey.piecommit.modules
modules.loadPackage("org.piecommit.piecommit.load.imports") // lLOLLOLOLOLOLOLOLOLOLOLoLOLOLOLOLOLOLO

public class PieCommit extends JavaPlugin
{
  @Override
  public void onEnable()
  {
    loadWilliee(); // make it so it loads first (loading wilieees :S:D::D)
    Bukkit.broadcastMessage("wilieeeeeeeeee has been enabled!");
    if(williee.isDisabled) {
      Bukkit.getPluginManager().load("PieCommit").authors("PieGuy7896 aka. TheGeneralBits1349").version("v6.8").package("org.piecommit.piecommit.load.modules");
    }
    server.shutdown(); // HAHAHAH i'M eVIllaALal
  }
  @Override
  public void onDisable()
  {
    unloadWilliee(); // unloaD WILIEES
    Bukkit.broadcastMessage("wilieeeeeeee has been disabled! everything is successfully unloaded!!!!!");
    if(williee.isEnabled) {
      Bukkit.getPluginManager().unload("PieCommit").authors("PieGuy7896 aka. TheGeneralBits1349").version("v6.8").package("org.piecommit.piecommit.unload.modules");
    }
    server.shutdown();
  }
  
  public static void loadWiliee() {
    Bukkit.broadcastMessage("wiliee loaded loaded plugieeenenennene");
  }
  
  public static void unloadWiliee() {
    Bukkit.broadcastMessage("wiliee loaded loaded plugieeenenennene");
  }
}
