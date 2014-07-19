package org.Random_TFM_Commands;

import org.bukkit.ChatColor;
import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;

@CommandPermissions(level = AdminLevel.ALL, source = SourceType.ONLY_IN_GAME)
@CommandParameters(description = "Because I have nothing better to do.", usage = "/<command>")
public class Command_hack extends TFM_Command
{
    
    @Override
    public boolean run(CommandSender sender, Player sender_p, Command cmd, String commandLabel, String[] args, boolean senderIsConsole)
    {
        sender_p.kickPlayer("m8 hacking is for nubs your Idiot");
        return true;
       
    }
}
