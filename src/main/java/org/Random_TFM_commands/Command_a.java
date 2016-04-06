package org.Random_TFM_Commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;

@CommandPermissions(level = AdminLevel.ALL, source = SourceType.ONLY_IN_GAME)
@CommandParameters(description = "", usage = "/<command>")
public class Command_a extends CommandExecutor<E>
{
    @Override
    public boolean onCommand(CommandSender sender, Player sender, Command cmd, String commandLabel, String[] args)
    {
        sender.sendMessage("");
        return true;
    }
}
