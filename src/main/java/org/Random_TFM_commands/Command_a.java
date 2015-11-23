package org.Random_TFM_Commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;

@CommandPermissions(level = AdminLevel.ALL, source = SourceType.ONLY_IN_GAME)
@CommandParameters(description = "Because I have nothing better to do.", usage = "/<command>")
public class Command_a extends CommandExecutor<Exts4>
{
    @Override
    public boolean run(CommandSender sender, Player sender_p, Command cmd, String commandLabel, String[] args, boolean senderIsConsole)
    {
        sender.sendMessage("");
        return true;
    }
}
