export const TabBarButton = ({ PageLink, Icon, Title }) => (
  <a href={ PageLink } class="grid text-white items-center justify-center">
    <div class="pb-2 px-auto justify-self-center">{Icon}</div>
    <span class="block font-medium text-xs">{ Title }</span>
  </a>
)