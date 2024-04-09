const newHandler = (data: Message) => {
  messages = [...messages, data];
  setTimeout(() => {
    scrollToBottom(messagesContainer);
  }, 100);
};

onMount(() => {
  pusherClient.subscribe($page.data.user.mail);
  pusherClient.bind("message:new", newHandler);

  scrollToBottom(messagesContainer);
});

