"""Setup the poker application"""
import logging

from poker.config.environment import load_environment
from poker.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup poker here"""
    load_environment(conf.global_conf, conf.local_conf)
    log.info("Creating tables")
    meta.metadata.create_all(bind=meta.engine)
    log.info("Successfully setup")


    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)
