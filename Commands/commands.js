module.exports = {
  name: 'commands',
  description: 'List all commands.',
  execute({ client, message }) {
    const commandNames = [...client.commands.keys()];
    message.channel.send(`Available commands:\n${commandNames.map(cmd => `!${cmd}`).join('\n')}`);
  }
};
