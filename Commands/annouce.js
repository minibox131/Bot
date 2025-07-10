module.exports = {
  name: 'announce',
  description: 'Send an announcement to a channel (mods only). Usage: !announce <channelID> <message>',
  execute({ client, message, args, modIDs }) {
    if (!modIDs.includes(message.author.id)) {
      return message.reply('You do not have permission to use this command.');
    }

    if (args.length < 2) {
      return message.reply('Usage: !announce <channelID> <message>');
    }

    const channelID = args.shift();
    const announcement = args.join(' ');

    const channel = client.channels.cache.get(channelID);
    if (!channel) {
      return message.reply('Invalid channel ID.');
    }

    channel.send(`📢 **Announcement:** ${announcement}`);
    message.reply('Announcement sent!');
  }
};
