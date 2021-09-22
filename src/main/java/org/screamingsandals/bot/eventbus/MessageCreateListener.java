package org.screamingsandals.bot.eventbus;

import discord4j.core.event.domain.message.MessageCreateEvent;
import org.screamingsandals.bot.commands.AbstractCommand;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.List;

@Service
public class MessageCreateListener extends AbstractEventListener<MessageCreateEvent> {
    private final String prefix;
    private final List<? extends AbstractCommand> commands;

    @Autowired
    public MessageCreateListener(List<? extends AbstractCommand> commands, Environment environment) {
        this.commands = commands;
        prefix = environment.getProperty("bot.prefix", "?");
    }

    @Override
    protected Mono<Void> handle(MessageCreateEvent event) {
        final String[] preprocessedInput = event.getMessage().getContent().split(" ");
        if (!preprocessedInput[0].startsWith(prefix)) {
            return Mono.empty();
        }
        preprocessedInput[0] = preprocessedInput[0].replaceFirst(prefix, "");
        return Flux.fromIterable(commands)
                .filter(command -> command.getName().equals(preprocessedInput[0]) && command.getArgs().size() == (preprocessedInput.length - 1))
                .flatMap(command -> command.handle(
                        command.getArgs().stream().map(argument -> argument.toInstance(preprocessedInput[command.getArgs().indexOf(argument) + 1])).toList()
                ))
                .onErrorResume(e -> Mono.empty())
                .next();

    }
}
